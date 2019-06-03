require k8s.io/client-go kubernetes-1.14.1
require k8s.io/api kubernetes-1.14.1
require k8s.io/apimachinery kubernetes-1.14.1

replace (
	k8s.io/api => k8s.io/api kubernetes-1.14.1
	k8s.io/apimachinery => k8s.io/apimachinery kubernetes-1.14.1
	k8s.io/client-go => k8s.io/client-go kubernetes-1.14.1
)
