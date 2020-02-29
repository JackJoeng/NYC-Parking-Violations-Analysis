from src.bigdata1.opcvapi import get_opcv, cat_opcv
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--page_size")
	parser.add_argument("--num_pages")
	parser.add_argument("--output")
	args = parser.parse_args()
	cat_opcv(args.output)
	get_opcv(args.page_size, args.num_pages, args.output)