source env/bin/activate
echo "Activated Virtual Environment"

echo "Running python server.."
echo "Executing server with settings path:"
python3 manage.py runserver

deactivate
echo "Virtual Environment deactivated"
echo "Closing server"