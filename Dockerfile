# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:latest

LABEL maintainer="Praveen Darshanam <praveend.hac@gmail.com>"

RUN apt-get update -y && apt-get install -y apt-utils vim wget netcat python3 python3-dev python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_ENV=development

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

