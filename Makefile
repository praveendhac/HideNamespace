# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# this will create go.mod
pre-requisite:
	go mod init github.com/HideNamespace

# will create go.sum and binary
# go build will build binary specific to the OS you are using
# to force build linux binary use "GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build"
build:
	go build
	docker build --no-cache -t praveendhac/hidenamespace:v1alpha1 .

push:
	docker push praveendhac/hidenamespace:v1alpha1

clean: 
	rm -rf HideNamespace 
