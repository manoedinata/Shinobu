echo "================================"
echo "          -> ndraBot <-          "
echo "================================"
echo

echo "Running the bot..."
gunicorn -w 3 -t 4 -b 0.0.0.0:8000 "wsgi:app"
