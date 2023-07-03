from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjMzMzFmNzJjZTlmZTJlMDg0NjIxZGExNmM0ZWNhMDk3Zjk1NTQ0NyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/S2S0ZDytY6yDm/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExODZkODczMDMyMzFjNWM1ZjVkOWY0MDVjYjAyYjg0NWU2ZDI4YmFhNyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/26uf43dkw9ByWsjLi/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmE0MDM3YjI2MjgzYzdiODU1YTFkOTVhZDc0ZDFjODU1NDJhOWNhNCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/wTrXRamYhQzsY/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDdiNTQzYmRjYjkyNTcwNzhhNjMzY2E0NjlkMjQ2MGUxNmE5ZGY4YSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/VzLR6oO6MzybC/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTExYmIxN2JmM2IxOTc4NmIwZmM4N2Y3MGE0ZWM0NDQzOTE3ZTM0NCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/U3PFGB8kCBVf7EN4Fk/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzFlYzZlNDc1NDFlMzZiZjE3YmQyZjFjZWZjZWFlMjM4NTdkYzgzNCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/1xONIE9kieqf4VTX50/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2U2NDNiZmQ4Mjc4Y2VmNjcyZWQyMzIyODgyM2RhYzEzNDIzMTFiMiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/l3vRmiPDHYMxn9Eys/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTczN2E1YmYyZWRiZjY0ODc1NDJkOWQ5MzQxNzI1OGQ1NTQ2NzgzNyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/18LZm8w9R8T0Q/giphy.gif",
]

@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
