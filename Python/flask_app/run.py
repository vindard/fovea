from handlers import app
import flask

app.run(debug=True,
        threaded=True,
        host='0.0.0.0',
        port=5000)