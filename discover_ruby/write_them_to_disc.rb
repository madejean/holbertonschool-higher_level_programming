require 'httpclient'
require "uri"

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 6e7f3146a1a9d7a12e4aceac3f3918c2fa57be6a'
}

clnt = HTTPClient.new

File.open("/tmp/22", "w") do |f|
    f.write(clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc'))
end
  

