from DrawingBoard.drawingBoard import DrawingBoard

# Drawing board dimension
width = 400
height = 400

if __name__ == "__main__":
    print("[*] starting drawing board...")
    draw = DrawingBoard(width, height)
    print("[+] drawing board started.")
    draw.start()
