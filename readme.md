# Eci libraries template.

This template has been created to help you to package your IBMTTS libraries in an independent add-on. By this way, the user can install libraries and the driver separately. So, when the user updates the driver, the libraries won't be lost.
If you copy the libraries in the add-on driver, an IBMTTS update will delete the libraries.

## Instructions to use this template.

1. Paste your libraries inside the "ECILibraries" folder.
2. go to the "ECILibraries" folder, select all the files and zip them. You can use
[7zip](https://www.7-zip.org/)
or any file compressor for this.
Remember that all the files must be placed in the zip root. It means that if you open the zip with the software compressor, the first thing that must be shown are the library files and not a folder.
3. Change the extension of the compressed file from ".zip" to ".nvda-addon".
4. Install the newly created add-on, it will automatically update the library paths in the NVDA settings. So, the IBMTTS driver will be able to find the library.
5. Optionally if you want, you can disable the newly installed add-on, is not required keep this add-on active.

Note: if your library dll is not named "eci.dll", you must specify the correct name in the "installTasks.py" file.

The file installTasks.py contains the process that set the correct NVDA settings to inform the driver where to fin the libraries.

## Disclaimer.
This template is intended to be used just with legal copies of the compiled binaries. Make sure that you have the license rights to distribute the libraries that you packaged in the add-on generated with this template.
I make no representation or warranty, express or implied. Your use of this template is solely at your own risk.
