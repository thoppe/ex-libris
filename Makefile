all:
	fab check
	fab thumbnails
	fab fullsize
	@make clean_junk

git:
	git status
	git commit -a
	git push

clean_junk:
	@find . -name "*.pyc" | xargs -I {} rm {}
	@find . -name "*~" | xargs -I {} rm {}
