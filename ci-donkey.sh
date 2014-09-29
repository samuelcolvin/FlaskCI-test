# continuous integration script fror FlaskCI
# <PRE SCRIPT>:
virtualenv env
echo "we haven't changed source so remember to manually call the correct python (or other script)"
echo "this is where you would install requirements and setup the enviroment"

echo "we have to copy the source into place since it's in a read only mounted volume"
cp /src/* .
sleep 90
# <MAIN SCRIPT>:
# python manage.py test
echo "now we're going to actually test the system"
./env/bin/python sample_test.py
