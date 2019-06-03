# HideNamespace
Hide Kubernetes Namespaceas

```
# delete Gopkg.toml, Gopkg.lock and vendor files/folders before running below command 
$ dep init
$ dep ensure -v
$ CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o HideNamespace .
```

## References
https://container-solutions.com/a-gentle-intro-to-validation-admission-webhooks-in-kubernetes/
https://container-solutions.com/some-admission-webhook-basics/
https://github.com/kubernetes/kubernetes/tree/v1.10.0-beta.1/test/images/webhook
https://docs.okd.io/latest/architecture/additional_concepts/dynamic_admission_controllers.html
https://docs.giantswarm.io/guides/creating-your-own-admission-controller/
https://banzaicloud.com/blog/k8s-admission-webhooks/
https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/
