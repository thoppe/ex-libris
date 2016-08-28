all:
	fab thumbnails
	@make clean_junk

git:
	git commit -a
	git push

clean_junk:
	@find . -name "*.pyc" | xargs -I {} rm {}
	@find . -name "*~" | xargs -I {} rm {}
