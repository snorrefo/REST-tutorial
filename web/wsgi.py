# Can either be called with
# python wsgi.py
# for running Flask development server with parameters given below, or
# gunicorn -w 4 -b 127.0.0.1:5001 wsgi:app
# for running gunicorn uwsgi server with 4 workers.

import flaskr

app = flaskr.create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
