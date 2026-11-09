> [!WARNING]
> **ARCHIVE / HISTORICAL DRAFT (OCTOBER 2026)**
> Этот документ является ранним историческим черновиком до архитектурного пивота 6–7 ноября 2026 г.
> Он содержит устаревшие концепции (серверный анализ аудиопотока YouTube, неструктурированные текстовые теги, старую концепцию «Better Spotify» и Spotify API).
> **Актуальные канонические материалы проекта находятся в папке `docs/`:**
> - Архитектура и протокол валидации: [`docs/validation_protocol.md`](../../docs/validation_protocol.md)
> - Полный отчёт: [`docs/report_text.md`](../../docs/report_text.md)

---

# Solution

> A website where producers can find sample recommendations based on section-specific categories in a full track.

---

## Q&A for Solution Description

### Who is it for?
Beginner producers, and producers with little free time.

### How does it work?
The purpose is to find a section of a song that matches your description, so that you can sample it in your own mixes.

### Where do songs come from?
Songs are not stored on the website — only YouTube links to them. Sections link to timed sections in YouTube videos, and a custom interface lets you click on a section to jump to that timestamp in the built-in YouTube player.

### How are song links stored on the site?
Not fully established yet; the idea is to draw on how review sites store individual track pages.

For now:
- Links are stored in a database, where each can be associated with one or more tags.
  - Example: a **Pop** tag contains *song X (at timestamp Y)*, *song Z (at timestamp Q)*, and so on.
- Links are stored alongside the **track title** and **artist name**, to prevent duplicates caused by different YouTube links to the same song.

### How do descriptions match?
1. You select a song. Some sections of it are highlighted.
2. These sections contain description tags that correlate with what happens in the section.
3. You select the tags that describe what you liked in the section.
4. You receive song recommendations. In each, you can go directly to the section that has the same (or at least one) of the descriptors you chose.
5. Clicking a song redirects you to the exact matching section.

Result: you've found a relevant sample from a completely different song. Instead of spending time browsing multiple songs until you find something usable, you go straight to the part that matches your request.

### Where do the tags come from?
Tags are submitted by other users.

- **Verification:** not fully planned yet. The first plan is:
  - a **report button** for false tags;
  - a **content moderation algorithm** to prevent offensive terms;
  - only **alphanumeric characters** allowed in tags.
- **Tag families:** when uploaded, tags are grouped into families based on instrumentation, effects, tone, frequency range, texture, and more.
- **Duplicates:** if two different tags have the same meaning and users report one for copying the other, one is deleted and all of its links are reattached to the surviving tag.

### How do other users submit tags?
Through a form on the original song's page, where the user:
- sets the time range of the section (**max 1 minute**);
- adds existing tags to it, **or** writes original ones and appeals them to an existing tag group.

Changes using existing tags are applied to the database **instantly**; new tags take **longer**, since they need moderation.

### So how do song recommendations work?
1. Clicking a highlighted section reveals the list of tags matched to that section.
2. After you select one or two of those tags, a list of suggestions appears. Each entry shows:
   - song title and artist name;
   - a visual showing where the highlighted section is in the recommended song;
   - which of the selected tags are present in that entry.
3. **Preventing empty results:** tags with no saved links are greyed out and shown separately from the others on the same section.

#### Ranking
- Results are ordered by **how many of the selected tags** they match.
- **Tag category** also matters: **instrument** tags are prioritized over the rest, so those results appear closer to the top.

#### Genre and metadata
- Song metadata such as genre has **no effect** on filtering unless the user explicitly selects it.
- When genre is selected, genre-matching results are prioritized above results of a different genre.
