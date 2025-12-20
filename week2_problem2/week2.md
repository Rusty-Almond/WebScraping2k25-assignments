### 1. Analyze DOM Structure 
 The DOM tree
 
``` 
html (lang="en-US")
├── head
│   ├── link (rel="stylesheet", href="styles.css")
│   └── title "MoviERA-Movie Recommendations"
└── body
    └── div.content
        ├── h1 "MoviERA"
        ├── h2 "The best movie recommendations out there"
        └── table.table-one (border="1", cellspacing="0", cellpadding="5")
            ├── tr (header row)
            │   ├── th "Movie Name"
            │   ├── th "Summary"
            │   ├── th "Genre(s)"
            │   ├── th "Duration"
            │   ├── th "Release Year"
            │   ├── th "IMdB rating"
            │   ├── th "Director"
            │   └── th "Trailer"
            ├── tr (movie row 1: Dune: Part Two)
            │   ├── td
            │   │   ├── span (style="font-size:20px")
            │   │   │   └── div.title "Dune:Part Two"
            │   │   └── img (src="...", alt="Dune:Part Two Poster", width=300, height=400)
            │   ├── td (summary)
            │   ├── td
            │   │   └── div.genre "Action / Adventure / Drama"
            │   ├── td "2h 46m"
            │   ├── td "2024"
            │   ├── td "8.7"
            │   ├── td "Denis Villeneuve"
            │   └── td.video
            │       └── div.video-wrapper
            │           └── iframe (src="Dune Trailer URL", allowfullscreen, title="Dune:Part Two Trailer")
            ├── tr (movie row 2: Oppenheimer)
            │   ├── td
            │   │   ├── span
            │   │   │   └── div.title "Oppenheimer"
            │   │   └── img (...)
            │   ├── td (summary)
            │   ├── td
            │   │   └── div.genre "Biography / Drama / History"
            │   ├── td "3h"
            │   ├── td "2023"
            │   ├── td "8.3"
            │   ├── td "Christopher Nolan"
            │   └── td.video
            │       └── div.video-wrapper
            │           └── iframe (src="Oppenheimer Trailer URL", allowfullscreen, title="Oppenheimer Trailer")
            └── tr (movie rows 3-5)
                └── ...
```

------

### 2. CSS Selectors

- Selector for body : `body`
- Selector for content : `.content`
- Selector for Heading 1 and 2 : `h1` and `h2`
- Selector for table : `.table-one`
- Selector for td in table: `.table-one td`
- Selector for titles for each movie name : `.title`
- Selector for videos : `video-wrapper`
- Selector for the genres : `.genre`

----

### 3. Role of attributes

They help in grouping elements (like `class`) , provide content links etc (like `src`,`href`) and are useful in providing the information which is  required to apply CSS to elements. This also helps in web scraping as we will get to know which part of the page we need to scrape to get the data we want.
