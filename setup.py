# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("rd6006/_version.py", "r") as fh:
    version = fh.readlines()[-1].split()[-1].strip("\"'")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rd6006",
    version=version,
    author="Baldanos",
    author_email="balda@balda.ch",
    description="Python bindings for RD6006",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baldanos/rd6006",
    packages=setuptools.find_packages(),
    install_requires=['pyserial', 'minimalmodbus'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)                                                                                   
