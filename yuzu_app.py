import yuzu_frontend
import yuzu_backend

def main():
    args = yuzu_frontend.main()
    if args[1]:
        yuzu_backend.main(args[0])

if __name__ == "__main__":
    main()