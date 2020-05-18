#!/usr/bin/env python3
# coding: utf-8
"""
    :author: Pratik K
    :brief: Basic fastAPI template with async mongodb support
"""
from sys import argv as rd
from app import app
from config import DEBUG


def main():
    try:
        port = int(rd[1])
    except:
        port = 8080
    finally:
        app.run(host='0.0.0.0', port=port, debug=DEBUG)


if __name__ == "__main__":
    main()
