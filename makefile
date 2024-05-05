VERSION ?= latest
BASE_IMAGE_NAME = us-central1-docker.pkg.dev/sigma-zodiac-422115-r8/medivise/api

build:
	docker build --platform linux/amd64 -t $(BASE_IMAGE_NAME):$(VERSION) .

create-tag:
	git tag -a $(VERSION) -m "Release $(VERSION)"
	git push origin $(VERSION)

publish: build
publish:
	docker push $(BASE_IMAGE_NAME):$(VERSION)
	make create-tag

deploy:
	helmfile apply --file helm/helmfile.yaml
