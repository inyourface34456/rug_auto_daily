echo -e "MAKE SURE TO ENABLE VPN\npress enter to continue..."
read _

source .venv/bin/activate
xargs -n3 python3 main.py < args.txt
