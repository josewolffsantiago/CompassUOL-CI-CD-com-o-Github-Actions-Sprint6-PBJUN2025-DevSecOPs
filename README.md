https://dev.to/bravinsimiyu/how-to-dockerize-and-deploy-a-fast-api-application-to-kubernetes-cluster-35a9


https://www.youtube.com/watch?v=DA6gywtTLL8&t=380s

https://docs.github.com/pt/actions/tutorials/use-containerized-services/create-a-docker-container-action

v1
https://medium.com/@ons.arouriii/deploying-a-fastapi-application-with-argo-cd-in-a-kubernetes-cluster-8900e610987a


V2
https://medium.com/@spiegelhaltercurt/end-to-end-ci-cd-with-argocd-github-actions-and-fastapi-on-kubernetes-8fdcab6c12df

https://shunya-vichaar.medium.com/guide-to-deploying-fastapi-with-helm-on-kubernetes-6529cdd147e5


        argocd app create hello-app     --repo https://github.com/josewolffsantiago/CompassUOL-CI-CD-ArgoCD-Sprint6-PBJUN2025-DevSecOPs.git     --path gitops-microservices/k8s/     --dest-server https://kubernetes.default.svc     --dest-namespace hello-app
