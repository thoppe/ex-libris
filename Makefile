SRCS := $(shell find . -name "*.xcf")
PNGS := $(addprefix thumbnails/,$(addsuffix .png,$(notdir $(basename $(SRCS)))))

all:
	make -j thumbnails

git:
	git commit -a
	git push

thumbnails: $(PNGS)	

$(PNGS) : $(SRCS)
	@mkdir -p thumbnails
	xcf2png --full-image --full-image $< > $@
	mogrify -thumbnail x300 $@
