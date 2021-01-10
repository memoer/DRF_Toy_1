read -n1 -p "[1] run [2] migrate [3] shell " t

case $t in
  1) python3 ./manage.py runserver ;;
  2) python3 ./manage.py makemigrations && python3 ./manage.py migrate ;;
  3) python3 ./manage.py shell ;;
esac
