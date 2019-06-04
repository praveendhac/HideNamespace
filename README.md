# HideNamespace
Hide Kubernetes Namespaceas

```
# create directory to code (HideNamespace here) anywhere on the disk 
$ go mod init github.com/HideNamespace
$ go build 
or
$ GO111MODULE=on CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o HideNamespace .
```

Test run of the created docker image from make build/make push
```
kubectl run pd-test --image=praveendhac/hidenamespace:v1alpha1 --rm -it --restart=Never -n my-namespace
```
## References
- https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/
- https://container-solutions.com/a-gentle-intro-to-validation-admission-webhooks-in-kubernetes/
- https://container-solutions.com/some-admission-webhook-basics/
- https://github.com/kubernetes/kubernetes/tree/v1.10.0-beta.1/test/images/webhook
- https://docs.okd.io/latest/architecture/additional_concepts/dynamic_admission_controllers.html
- https://docs.giantswarm.io/guides/creating-your-own-admission-controller/
- https://banzaicloud.com/blog/k8s-admission-webhooks/
- https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/
