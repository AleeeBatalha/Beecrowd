while True:
    try:
        n = int(input())
        
        for i in range(1, n + 1):
            resposta = input().strip()
            print(f"resposta {i}: {resposta}")
    except EOFError:
        break
