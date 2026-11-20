#!/usr/bin/env python3
"""
Interactive Transcript Viewer for WhisperX JSON Outputs.
Supports dialogue reading with pager, speaker grouping, search, stats, and markdown export.
"""

import sys
import os
import json
import glob
import re

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


def format_time(seconds: float) -> str:
    """Format seconds into HH:MM:SS or MM:SS."""
    secs = int(round(seconds))
    hrs = secs // 3600
    mins = (secs % 3600) // 60
    rem_secs = secs % 60
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{rem_secs:02d}"
    return f"{mins:02d}:{rem_secs:02d}"


class TranscriptViewer:
    SPEAKER_COLORS = {
        "SPEAKER_00": "bold cyan",
        "SPEAKER_01": "bold green",
        "SPEAKER_02": "bold yellow",
        "SPEAKER_03": "bold magenta",
        "UNKNOWN": "bold white",
    }

    def __init__(self, base_dir: str = None):
        self.base_dir = base_dir or os.path.dirname(os.path.abspath(__file__))
        self.console = Console() if RICH_AVAILABLE else None
        self.files = self._find_files()
        self.current_data = None
        self.current_file = None

    def _find_files(self):
        pattern = os.path.join(self.base_dir, "*.json")
        return sorted([f for f in glob.glob(pattern) if not f.endswith("_old.json")])

    def print_msg(self, msg: str, style: str = ""):
        if self.console and style:
            self.console.print(msg, style=style)
        elif self.console:
            self.console.print(msg)
        else:
            print(msg)

    def load_file(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            self.current_data = json.load(f)
        self.current_file = filepath

    def get_turns(self, max_gap: float = 2.0):
        """Group consecutive segments of the same speaker into dialogue turns."""
        if not self.current_data or "segments" not in self.current_data:
            return []

        turns = []
        current_turn = None

        for seg in self.current_data["segments"]:
            speaker = seg.get("speaker", "UNKNOWN")
            start = seg.get("start", 0.0)
            end = seg.get("end", 0.0)
            text = seg.get("text", "").strip()

            if not text:
                continue

            if (current_turn is not None and 
                current_turn["speaker"] == speaker and 
                (start - current_turn["end"]) <= max_gap):
                current_turn["end"] = end
                current_turn["text"] += " " + text
                current_turn["segments"].append(seg)
            else:
                if current_turn is not None:
                    turns.append(current_turn)
                current_turn = {
                    "speaker": speaker,
                    "start": start,
                    "end": end,
                    "text": text,
                    "segments": [seg]
                }

        if current_turn is not None:
            turns.append(current_turn)

        return turns

    def show_dialogue(self):
        """Display readable grouped dialogue using terminal pager."""
        turns = self.get_turns()
        if not turns:
            self.print_msg("[red]No segments found in file.[/red]")
            return

        title = os.path.basename(self.current_file)
        dur = turns[-1]["end"] if turns else 0

        if self.console:
            with self.console.pager(styles=True):
                self.console.print(Panel(f"[bold white]{title}[/bold white]\nDuration: {format_time(dur)} | Total Turns: {len(turns)}", style="blue"))
                self.console.print()
                for turn in turns:
                    spk = turn["speaker"]
                    color = self.SPEAKER_COLORS.get(spk, "white")
                    time_str = f"[{format_time(turn['start'])} - {format_time(turn['end'])}]"
                    self.console.print(f"[dim]{time_str}[/dim] [{color}]{spk}[/{color}]:")
                    self.console.print(f"  {turn['text']}\n")
        else:
            print(f"=== {title} ({format_time(dur)}) ===")
            for turn in turns:
                time_str = f"[{format_time(turn['start'])} - {format_time(turn['end'])}]"
                print(f"{time_str} {turn['speaker']}:")
                print(f"  {turn['text']}\n")

    def show_segments_table(self, speaker_filter: str = None):
        """Display individual segments in a table."""
        segs = self.current_data.get("segments", [])
        if speaker_filter:
            segs = [s for s in segs if s.get("speaker") == speaker_filter]

        if not segs:
            self.print_msg(f"[yellow]No segments found matching filter '{speaker_filter}'.[/yellow]")
            return

        if self.console:
            table = Table(title=f"Segments - {os.path.basename(self.current_file)}", box=box.ROUNDED)
            table.add_column("#", style="dim", width=5)
            table.add_column("Start", style="cyan", width=8)
            table.add_column("End", style="cyan", width=8)
            table.add_column("Speaker", style="bold", width=12)
            table.add_column("Text", style="white")

            for idx, s in enumerate(segs):
                spk = s.get("speaker", "UNKNOWN")
                color = self.SPEAKER_COLORS.get(spk, "white")
                table.add_row(
                    str(idx + 1),
                    format_time(s.get("start", 0)),
                    format_time(s.get("end", 0)),
                    f"[{color}]{spk}[/{color}]",
                    s.get("text", "").strip()
                )

            with self.console.pager(styles=True):
                self.console.print(table)
        else:
            for idx, s in enumerate(segs):
                print(f"{idx+1:4d} | {format_time(s.get('start',0))} - {format_time(s.get('end',0))} | {s.get('speaker')}: {s.get('text', '').strip()}")

    def search_transcript(self):
        """Search transcript by keyword or regex."""
        segs = self.current_data.get("segments", [])
        query = input("\nEnter search query (word or phrase): ").strip()
        if not query:
            return

        regex = re.compile(re.escape(query), re.IGNORECASE)
        matches = []

        for idx, s in enumerate(segs):
            text = s.get("text", "")
            if regex.search(text):
                matches.append((idx, s))

        if not matches:
            self.print_msg(f"\n[yellow]No matches found for '{query}'.[/yellow]")
            input("Press Enter to continue...")
            return

        self.print_msg(f"\n[green]Found {len(matches)} matches for '{query}':[/green]\n")
        for num, (idx, s) in enumerate(matches, 1):
            time_str = f"[{format_time(s.get('start', 0))} - {format_time(s.get('end', 0))}]"
            spk = s.get("speaker", "UNKNOWN")
            color = self.SPEAKER_COLORS.get(spk, "white")
            highlighted = regex.sub(lambda m: f"[bold red on yellow]{m.group(0)}[/bold red on yellow]", s.get("text", "").strip())
            if self.console:
                self.console.print(f" {num:2d}. [dim]Seg #{idx+1}[/dim] [dim]{time_str}[/dim] [{color}]{spk}[/{color}]:")
                self.console.print(f"     {highlighted}\n")
            else:
                print(f" {num:2d}. Seg #{idx+1} {time_str} {spk}: {s.get('text','').strip()}\n")

        input("Press Enter to continue...")

    def show_statistics(self):
        """Show speaker breakdown and timing statistics."""
        segs = self.current_data.get("segments", [])
        total_dur = segs[-1]["end"] if segs else 0
        total_words = sum(len(s.get("words", [])) for s in segs)

        stats = {}
        for s in segs:
            spk = s.get("speaker", "UNKNOWN")
            dur = s.get("end", 0) - s.get("start", 0)
            words = len(s.get("words", []))
            if spk not in stats:
                stats[spk] = {"duration": 0.0, "words": 0, "segments": 0}
            stats[spk]["duration"] += dur
            stats[spk]["words"] += words
            stats[spk]["segments"] += 1

        if self.console:
            table = Table(title=f"Statistics - {os.path.basename(self.current_file)}", box=box.ROUNDED)
            table.add_column("Speaker", style="bold")
            table.add_column("Segments", justify="right")
            table.add_column("Words", justify="right")
            table.add_column("Words %", justify="right")
            table.add_column("Speaking Time", justify="right")
            table.add_column("Time %", justify="right")

            for spk, st in sorted(stats.items()):
                w_pct = (st["words"] / total_words * 100) if total_words else 0
                t_pct = (st["duration"] / total_dur * 100) if total_dur else 0
                color = self.SPEAKER_COLORS.get(spk, "white")
                table.add_row(
                    f"[{color}]{spk}[/{color}]",
                    str(st["segments"]),
                    str(st["words"]),
                    f"{w_pct:.1f}%",
                    format_time(st["duration"]),
                    f"{t_pct:.1f}%"
                )

            summary = Panel(
                f"[bold]Total Duration:[/bold] {format_time(total_dur)}  |  "
                f"[bold]Total Words:[/bold] {total_words}  |  "
                f"[bold]Total Segments:[/bold] {len(segs)}",
                style="green"
            )
            self.console.print()
            self.console.print(table)
            self.console.print(summary)
        else:
            print(f"\n--- Statistics: {os.path.basename(self.current_file)} ---")
            for spk, st in stats.items():
                print(f"{spk}: {st['segments']} segs, {st['words']} words, {format_time(st['duration'])}")

        input("\nPress Enter to continue...")

    def export_markdown(self):
        """Export current transcript as clean formatted Markdown."""
        turns = self.get_turns()
        base_name = os.path.splitext(self.current_file)[0]
        out_path = base_name + ".md"

        dur = turns[-1]["end"] if turns else 0
        lines = [
            f"# Transcript: {os.path.basename(base_name)}",
            f"- **Duration:** {format_time(dur)}",
            f"- **Turns:** {len(turns)}",
            "",
            "---",
            ""
        ]

        for turn in turns:
            time_str = f"{format_time(turn['start'])} - {format_time(turn['end'])}"
            lines.append(f"### `{time_str}` **{turn['speaker']}**")
            lines.append(f"{turn['text']}")
            lines.append("")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        self.print_msg(f"\n[green]Saved Markdown transcript to: {out_path}[/green]")
        input("Press Enter to continue...")

    def export_all_markdown(self):
        """Export all JSON files to markdown."""
        for f in self.files:
            self.load_file(f)
            turns = self.get_turns()
            base_name = os.path.splitext(f)[0]
            out_path = base_name + ".md"
            dur = turns[-1]["end"] if turns else 0
            lines = [
                f"# Transcript: {os.path.basename(base_name)}",
                f"- **Duration:** {format_time(dur)}",
                f"- **Turns:** {len(turns)}",
                "",
                "---",
                ""
            ]
            for turn in turns:
                time_str = f"{format_time(turn['start'])} - {format_time(turn['end'])}"
                lines.append(f"### `{time_str}` **{turn['speaker']}**")
                lines.append(f"{turn['text']}")
                lines.append("")
            with open(out_path, "w", encoding="utf-8") as out_fp:
                out_fp.write("\n".join(lines))
            self.print_msg(f"Exported: {os.path.basename(out_path)}")

    def run_file_menu(self):
        while True:
            if self.console:
                self.console.clear()
            fname = os.path.basename(self.current_file)
            dur = self.current_data["segments"][-1]["end"] if self.current_data.get("segments") else 0
            
            menu_text = (
                f"[bold white]{fname}[/bold white] ([dim]{format_time(dur)}[/dim])\n\n"
                "[bold cyan]1.[/bold cyan] Read Dialogue (Paged Reader - use arrow keys, 'q' to exit)\n"
                "[bold cyan]2.[/bold cyan] View Segments Table\n"
                "[bold cyan]3.[/bold cyan] Search in Transcript\n"
                "[bold cyan]4.[/bold cyan] Speaker & Time Statistics\n"
                "[bold cyan]5.[/bold cyan] Export to Markdown (.md)\n"
                "[bold cyan]6.[/bold cyan] Back to File Selection\n"
                "[bold cyan]0.[/bold cyan] Exit\n"
            )
            if self.console:
                self.console.print(Panel(menu_text, title="Transcript Menu", style="blue"))
            else:
                print(f"\n=== {fname} ===")
                print("1. Read Dialogue")
                print("2. View Segments Table")
                print("3. Search in Transcript")
                print("4. Statistics")
                print("5. Export to Markdown")
                print("6. Back")
                print("0. Exit")

            choice = input("Select an option (1-6, 0): ").strip()
            if choice == "1":
                self.show_dialogue()
            elif choice == "2":
                spk = input("Filter by speaker (e.g. SPEAKER_00) or press Enter for all: ").strip()
                self.show_segments_table(spk if spk else None)
            elif choice == "3":
                self.search_transcript()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                self.export_markdown()
            elif choice == "6":
                break
            elif choice == "0":
                sys.exit(0)

    def run(self):
        if not self.files:
            self.print_msg(f"[red]No JSON transcripts found in {self.base_dir}[/red]")
            return

        while True:
            if self.console:
                self.console.clear()
                table = Table(title="Available Normalized Transcripts", box=box.ROUNDED)
                table.add_column("#", style="cyan", width=4)
                table.add_column("Filename", style="bold white")
                table.add_column("Duration", style="yellow")
                table.add_column("Segments", justify="right")
                table.add_column("Words", justify="right")

                for idx, path in enumerate(self.files, 1):
                    with open(path, "r", encoding="utf-8") as f:
                        d = json.load(f)
                    dur = d["segments"][-1]["end"] if d.get("segments") else 0
                    words = sum(len(s.get("words", [])) for s in d.get("segments", []))
                    table.add_row(
                        str(idx),
                        os.path.basename(path),
                        format_time(dur),
                        str(len(d.get("segments", []))),
                        str(words)
                    )
                self.console.print(table)
                self.console.print("\n[bold cyan]E.[/bold cyan] Export all transcripts to Markdown (.md)")
                self.console.print("[bold cyan]0.[/bold cyan] Exit\n")
            else:
                print("\nAvailable Normalized Transcripts:")
                for idx, path in enumerate(self.files, 1):
                    print(f"[{idx}] {os.path.basename(path)}")
                print("[E] Export all to Markdown")
                print("[0] Exit")

            choice = input("Choose file # (or E/0): ").strip().upper()
            if choice == "0":
                break
            elif choice == "E":
                self.export_all_markdown()
                input("\nAll files exported! Press Enter to continue...")
                continue
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.files):
                    self.load_file(self.files[idx])
                    self.run_file_menu()
                else:
                    input("Invalid selection. Press Enter...")
            except ValueError:
                input("Invalid input. Press Enter...")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--export":
            viewer = TranscriptViewer()
            viewer.export_all_markdown()
            sys.exit(0)
        elif os.path.isfile(sys.argv[1]):
            viewer = TranscriptViewer()
            viewer.load_file(sys.argv[1])
            viewer.run_file_menu()
            sys.exit(0)

    viewer = TranscriptViewer()
    viewer.run()
