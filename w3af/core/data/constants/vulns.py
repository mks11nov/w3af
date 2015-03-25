"""
vulns.py

Copyright 2012 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
VULNS = {
         00000: 'TestCase',

         # Audit
         10000: 'Blind SQL injection vulnerability',
         10001: 'Buffer overflow vulnerability',
         10002: 'Multiple CORS misconfigurations',
         10003: 'Sensitive and strange CORS methods enabled',
         10004: 'Sensitive CORS methods enabled',
         10005: 'Uncommon CORS methods enabled',
         10006: 'Access-Control-Allow-Origin set to "*"',
         10007: 'Insecure Access-Control-Allow-Origin with credentials',
         10008: 'Insecure Access-Control-Allow-Origin',
         10009: 'Incorrect withCredentials implementation',
         10010: 'CSRF vulnerability',
         10011: 'Insecure DAV configuration',
         10012: 'DAV incorrect configuration',
         #10013: 'Vacant',
         #10014: 'Vacant',
         10015: 'Insecure file upload',
         10016: 'Format string vulnerability',
         10017: 'Insecure Frontpage extensions configuration',
         #10018: 'Vacant',
         10019: 'Unhandled error in web application',
         10020: 'Insecure redirection',
         10021: 'Misconfigured access control',
         10022: 'LDAP injection vulnerability',
         10023: 'Local file inclusion vulnerability',
         10024: 'File read error',
         10025: 'MX injection vulnerability',
         10026: 'OS commanding vulnerability',
         10027: 'Phishing vector',
         10028: 'Unsafe preg_replace usage',
         10029: 'ReDoS vulnerability',
         #10030: 'Vacant',
         10031: 'Response splitting vulnerability',
         10032: 'Remote code execution',
         10033: 'Remote file inclusion',
         10034: 'Potential remote file inclusion',
         10035: 'SQL injection',
         10036: 'Server side include vulnerability',
         10037: 'Persistent server side include vulnerability',
         10038: 'Insecure SSL version',
         10039: 'Invalid SSL certificate',
         10041: 'Invalid SSL connection',
         10042: 'Soon to expire SSL certificate',
         10043: 'SSL Certificate dump',
         10044: 'Secure content over insecure channel',
         10045: 'XPATH injection vulnerability',
         10046: 'Persistent Cross-Site Scripting vulnerability',
         10047: 'Cross site scripting vulnerability',
         10048: 'Cross site tracing vulnerability',
         10049: 'Parameter modifies response headers',
         10050: 'eval() input injection vulnerability',
         10051: 'Reflected File Download vulnerability',
         10052: 'Shell shock vulnerability',
         
         # Crawl
         20000: 'phpinfo() file found',
         20001: 'PHP register_globals: On',
         20002: 'PHP allow_url_fopen: On',
         20003: 'PHP allow_url_include: On',
         20004: 'PHP display_errors: On',
         20005: 'PHP expose_php: On',
         20006: 'PHP lowest_privilege_test:fail',
         20007: 'PHP disable_functions:few',
         20008: 'PHP curl_file_support:not_fixed',
         20009: 'PHP cgi_force_redirect: Off',
         20010: 'PHP session.cookie_httponly: Off',
         20011: 'PHP session_save_path:Everyone',
         20012: 'PHP session_use_trans: On',
         20013: 'PHP default_charset: Off',
         20014: 'PHP enable_dl: On',
         20015: 'PHP memory_limit:high',
         20016: 'PHP post_max_size:high',
         20017: 'PHP upload_max_filesize:high',
         20018: 'PHP upload_tmp_dir:Everyone',
         20019: 'PHP file_uploads: On',
         20020: 'PHP magic_quotes_gpc: On',
         20021: 'PHP magic_quotes_gpc: Off',
         20022: 'PHP open_basedir:disabled',
         20023: 'PHP open_basedir:enabled',
         20024: 'PHP session.hash_function:md5',
         20025: 'PHP session.hash_function:sha',
         20026: 'Insecure resource',
         20027: '.listing file found',
         20028: 'Operating system username and group leak',
         20029: 'Google hack database match',
         20030: 'Phishing scam',
         20031: 'Source code repository',
         20032: 'Insecure RIA settings',
         20033: 'Cross-domain allow ACL',
         20034: 'Potential web backdoor',
         20035: 'Captcha image detected',
         20036: 'Oracle Application Server',
         20037: 'Potentially interesting file',
         20038: 'urllist.txt file',
         20039: 'Fingerprinted operating system',
         20040: 'Identified installed application',
         20041: 'robots.txt file',
         20042: 'HTTP Content Negotiation enabled',
         20043: 'Fingerprinted Wordpress version',
         20044: 'Gears manifest resource',
         20045: 'Invalid RIA settings file',
         20046: 'Identified WordPress user',
         20047: 'WordPress path disclosure',
         20048: 'PHP register_globals: Off',
         20049: 'PHP enable_dl: Off',
         20050: 'Web user home directory',
         
         # Grep
         30001: 'US Social Security Number disclosure',
         30002: 'DOM Cross site scripting',
         30003: 'Parameter has SQL sentence',
         30004: 'Uncommon query string parameter',
         30005: 'Credit card number disclosure',
         30006: 'Code disclosure vulnerability',
         30007: 'Code disclosure vulnerability in 404 page',
         30008: 'Unhandled error in web application',
         30009: 'Basic HTTP credentials',
         30010: 'Authentication without www-authenticate header',
         30011: 'NTLM authentication',
         30012: 'HTTP Basic authentication',
         # 30013 was a duplicate, I can re-use it in the future
         #30013: 'Vacant',
         30014: 'Cookie without HttpOnly',
         30015: 'Secure cookie over HTTP',
         30016: 'Secure flag missing in HTTPS cookie',
         30017: 'Secure cookies over insecure channel',
         30018: 'Identified cookie',
         30019: 'Cookie',
         30020: 'Invalid cookie',
         30021: 'Click-Jacking vulnerability',
         30022: 'Private IP disclosure vulnerability',
         30023: 'Directory indexing',
         30024: 'Path disclosure vulnerability',
         30025: 'Missing cache control for HTTPS content',
         30026: 'SVN user disclosure vulnerability',
         30027: 'HTTP Request in HTTP body',
         30028: 'HTTP Response in HTTP body',
         30029: 'Auto-completable form',
         30030: 'Session ID in URL',
         30031: 'WSDL resource',
         30032: 'DISCO resource',
         30033: 'Symfony Framework with CSRF protection disabled',
         30034: 'Descriptive error page',
         30035: 'Error page with information disclosure',
         30036: 'Oracle application server',
         30037: 'Strange header',
         30038: 'Content-Location HTTP header anomaly',
         30039: '.NET Event Validation is disabled',
         30040: '.NET ViewState encryption is disabled',
         30041: 'Exposed email address',
         30042: 'Interesting HTML comment',
         30043: 'HTML comment contains HTML code',
         30044: 'Strange HTTP response code',
         30045: 'File upload form',
         #30046: 'Vacant',
         30047: 'Interesting META tag',
         30048: 'User defined regular expression match',
         30049: 'Mark of the web',
         30050: 'Cross-domain javascript source',
         30051: 'Insecure X-XSS-Protection header usage',
         30052: 'Browser plugin content',
         30053: 'Strange HTTP Reason message',
         30054: 'Hash string in HTML content',
         30055: 'Blank http response body',
         30056: 'Content feed resource',
         30057: 'Malware identified',
         30058: 'Insecure password submission over HTTP',
         30059: 'CSP vulnerability',
         30060: 'Missing X-Content-Type-Options header',
         30061: 'Missing Strict Transport Security header',
         30062: 'HTML5 WebSocket detected',
         30063: 'Insecure password form access over HTTP',
         
         # Infrastructure
         40001: 'Potential XSS vulnerability',
         40002: 'HTTP and HTTPs hop distance',
         40003: 'HTTP traceroute',
         40004: 'Apache Server version',
         40005: 'Shared hosting',
         40006: 'Virtual host identified',
         40007: 'Previous defacements',
         40008: 'Email account',
         40009: 'Internal hostname in HTML link',
         40011: 'Default virtual host',
         40012: 'No DNS wildcard',
         40013: 'DNS wildcard',
         40014: 'Webserver fingerprint',
         40015: 'Web Application Firewall fingerprint',
         40016: 'FrontPage configuration information',
         40017: 'Customized frontpage configuration',
         40018: 'FrontPage FPAdminScriptUrl',
         40019: 'Operating system',
         40020: 'Favicon identification',
         40021: 'Favicon identification failed',
         40022: 'Transparent proxy detected',
         40023: 'PHP Egg',
         40024: 'Fingerprinted PHP version',
         40025: 'Server header',
         40026: 'Omitted server header',
         40027: 'Powered-by header',
         40028: 'Non existent methods default to GET',
         40029: 'DAV methods enabled',
         40030: 'Active filter detected',
         40031: 'Reverse proxy identified',
         40032: 'HTTP load balancer detected',
         40033: 'Information disclosure via .NET errors',
         40034: 'Potential virtual host misconfiguration',
         
         # Bruteforce
         50000: 'Guessable credentials',

         # Attack
         60000: 'DAV Misconfiguration',
         60001: 'Arbitrary file upload',
         60002: 'OS Commanding code execution',
         60003: 'Code execution via remote file inclusion',
         60004: '(Blind) SQL injection',
         60005: 'Arbitrary file read',

         # Users can add their vulnerabilities
         70000: 'Manually added vulnerability',
                                    
         }


def is_valid_name(name):
    return name in VULNS.values()