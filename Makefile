command:
	git push origin main
	docker build -t arthurlimadossantos/flask-kubernetes:v${PARAMS} .
	docker push arthurlimadossantos/flask-kubernetes:v${PARAMS}
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/pod.yaml
	kubectl apply -f k8s/service.yaml
	kubectl port-forward svc/flaskserver-service 5000:5000