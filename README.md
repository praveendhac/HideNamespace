# HideNamespace
Hide Kubernetes Namespaces, though we have RBACs to control who can create, delete namespaces and deploy to namespaces but with this Webhook I don't want to show few namespaces to few clusters users based on config, somehow this is not possible because of the limitation explained in `RETIRED` file. 

## Build
```
# create directory to code (HideNamespace here) anywhere on the disk 
$ go mod init github.com/HideNamespace
$ go build 
or
$ GO111MODULE=on CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o HideNamespace .
```
Above commands if run on MacOS will build MacOS binary, to cross-compile i.e. build linux binary run
- Cross compile
```
$ GO111MODULE=on GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build
```

Test run of the created docker image from make build/make push
```
kubectl run pd-test --image=praveendhac/hidenamespace:v1alpha1 --rm -it --restart=Never -n my-namespace
```
## Certifying Authority
caBundle(CA_BUNDLE) is PEM encoded CA cert that signs webhook server cert. Generating CA_BUNDLE used in validating-webhook-conf.yaml.tmpl
```
cat ./deployment/validating-webhook-conf.yaml.tmpl | ./deployment/get_and_patch_wh_ca_bundle.sh > ./deployment/validating-webhook-conf-ca-bundle.yaml
```
Using secret generated using get_and_patch_wh_ca_bundle.sh as `caBundle` didn't work, instead used below Flask server cert.pem base64 encoded as `caBundle`
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem
cat cert.pem |base64
```

## HTTP vs HTTPS
I was trying to keep it simple, developing webhook server in HTTP but from below error message it looks we need to run webhook server which can understand HTTPS.
```
W0608 23:23:13.539938       1 dispatcher.go:68] Failed calling webhook, failing open hide-namespace.praveend.com: failed calling webhook "hide-namespace.praveend.com": Post https://hide-namespace-webhook-svc.hide-namespace.svc:443/hide-namespace?timeout=30s: no service port "443" found for service "hide-namespace-webhook-svc"
E0608 23:23:13.539962       1 dispatcher.go:69] failed calling webhook "hide-namespace.praveend.com": Post https://hide-namespace-webhook-svc.hide-namespace.svc:443/hide-namespace?timeout=30s: no service port "443" found for service "hide-namespace-webhook-svc"
```

## References
- https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/
- https://github.com/morvencao/kube-mutating-webhook-tutorial/blob/master/medium-article.md
- https://container-solutions.com/a-gentle-intro-to-validation-admission-webhooks-in-kubernetes/
- https://container-solutions.com/some-admission-webhook-basics/
- https://github.com/kubernetes/kubernetes/tree/v1.10.0-beta.1/test/images/webhook
- https://docs.okd.io/latest/architecture/additional_concepts/dynamic_admission_controllers.html
- https://docs.giantswarm.io/guides/creating-your-own-admission-controller/
- https://banzaicloud.com/blog/k8s-admission-webhooks/
- https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/
