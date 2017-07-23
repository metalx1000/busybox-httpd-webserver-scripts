#!/bin/sh

# POST upload format:
# -----------------------------29995809218093749221856446032^M
# Content-Disposition: form-data; name="file1"; filename="..."^M
# Content-Type: application/octet-stream^M
# ^M    <--------- headers end with empty line
# file contents
# file contents
# file contents
# ^M    <--------- extra empty line
# -----------------------------29995809218093749221856446032--^M

folder=../uploads/

CR=`printf '\r'`

# CGI output must start with at least empty line (or headers)
echo "Content-type: text/html"
printf '\r\n'

while read -r line; do
  #get file name of uploaded file
  echo "$line" | grep "filename" > /dev/null && file="$(echo "$line"|cut -d\" -f4)"
  test x"$line" = x"" && break
  test x"$line" = x"$CR" && break
done

echo "$file uploaded."
cat >"${folder}${file}"
