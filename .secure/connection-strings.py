config = {
    "external": {
        "service": "postgres://iustpg:rvEfWaVRkOO8fiSjLxxgx8EAX8ow75Xs@dpg-cl145bq35nfs739mv5t0-a.frankfurt-postgres.render.com/iustpg",
        "cmd": "PGPASSWORD=rvEfWaVRkOO8fiSjLxxgx8EAX8ow75Xs psql -h dpg-cl145bq35nfs739mv5t0-a.frankfurt-postgres.render.com -U iustpg iustpg"
    }
    "internal": {
        "service": "postgres://iustpg:rvEfWaVRkOO8fiSjLxxgx8EAX8ow75Xs@dpg-cl145bq35nfs739mv5t0-a/iustpg"
    }
}