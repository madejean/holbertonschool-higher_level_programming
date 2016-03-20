require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 6e7f3146a1a9d7a12e4aceac3f3918c2fa57be6a'
}

clnt = HTTPClient.new
list = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
 parse = JSON.parse(list)
puts parse['items'].map{ |name| name['full_name'] }.join("\n")
