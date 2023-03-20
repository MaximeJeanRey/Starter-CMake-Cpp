#include <iostream>
#include <string>
#include <cstdlib>

const std::size_t ENV_BUF_SIZE = 2048; // Enough for your PATH?

using namespace std;

int main()
{

    cout << "Hello World!" << endl;
    // char buf[ENV_BUF_SIZE];
    // std::size_t bufsize = ENV_BUF_SIZE;
    // int e = getenv_s(&bufsize,buf,bufsize,"PATH");  
    // if (e) {
    //     std::cerr << "`getenv_s` failed, returned " << e << '\n';
    //     exit(EXIT_FAILURE);
    // }
    // std::string env_path = buf;
    // std::cout << "In main process, `PATH`=" << env_path << std::endl;
    // env_path += ";C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\VC\\bin\\amd64";
    // e = _putenv_s("PATH",env_path.c_str());
    // if (e) {
    //     std::cerr << "`_putenv_s` failed, returned " << e << std::endl;
    //     exit(EXIT_FAILURE);
    // }
    // std::cout << std::endl;
    // e = std::system("echo \"In child process `PATH`=%PATH%\"");
    // if (e) {
    //     std::cerr << "`std::system` failed, returned " << e << std::endl;
    //     exit(EXIT_FAILURE);
    // }
    return 0;
}