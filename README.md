# fastapi-graphql-postgres-exemplar

## Run exemplar

First run these commands to get everything running.

```bash
virtualenv -p python 3.10 venv
. venv/bin/activate
pip install -r requirements.txt
docker compose up
uvicorn main:app
```

Then open http://127.0.0.1:8000/graphql and run the following query

```
query MyQuery {
  members(customInformationFilter: {customField: "favoriteNumber", customValue: 3}) {
    age
    customInformation
    id
    name
  }
}
```

It will return all the Beatles members that have `3` as their favorite number.