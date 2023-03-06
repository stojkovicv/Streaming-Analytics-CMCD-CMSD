# cmcd-server
locust -f locust.py --host http://localhost:5500/stream-client/ --users 10000 --spawn-rate 5000

# cmcd-bridge
# locust -f locust.py --host http://localhost:8088 --users 100 --spawn-rate 80
