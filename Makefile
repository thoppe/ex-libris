books = TwentyThousandLeagues TheCallOfCthulhu 1984 HarryPotter ATaleOfTwoCities

all:
	echo $(books)

git:
	git commit -a
	git push

thumbnail:
	mkdir -p thumbnails

	for x in $(books); do \
		echo $$x ;\
		xcf2png --full-image --full-image $$x.xcf > $$x.png ;\
		convert -thumbnail x300 $$x.png thumbnails/$$x.png ;\
		rm $$x.png ;\
	done



