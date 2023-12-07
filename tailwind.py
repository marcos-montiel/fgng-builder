import subprocess


def main():
    subprocess.run(
        [
            "bun",
            "run",
            "tailwindcss",
            "-i",
            "./static/src/input.css",
            "-o",
            "./static/src/output.css",
        ]
    )


if __name__ == "__main__":
    main()
