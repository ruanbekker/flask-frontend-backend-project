# flask-frontend-backend-project
Frontend (UI) and Backend (API) using Flask Example

## Request Flow

```
UI -> QueryParam: /?keyword=[string] -> Request to Backend API -> Matches [string] in dataset -> Returns to Frontend
```

## Searchable Data

The search query runs against the "project_text" key in [backend/data.json](backend/data.json)

## Screenshots

When opening the UI:

<img width="1007" alt="image" src="https://user-images.githubusercontent.com/567298/66004815-04589c00-e4aa-11e9-9845-2312862ba1f0.png">

Searching for "will" (there will be 2 results)

<img width="1001" alt="image" src="https://user-images.githubusercontent.com/567298/66004848-13d7e500-e4aa-11e9-88fb-93c172f19145.png">

When searching for "project" will show all the results as every result has the value:

<img width="1022" alt="image" src="https://user-images.githubusercontent.com/567298/66004891-29e5a580-e4aa-11e9-98be-a10d9800874c.png">
