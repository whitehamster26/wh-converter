<h1>Simple CLI currency converter</h1>
<p>In this app I use <a href="https://www.alphavantage.co/">alphavantage</a> API.</p>
<p>By default you'd use standart API key that I share with users of this app</p>
<p>Alphavantage has some limit of using its API so you <a href="https://www.alphavantage.co/support/#api-key">can register</a> your free API key and use it in this app using <code>wh-conv --apikey [KEY]</code></p>

<h2>Badges</h2>
[![Maintainability](https://api.codeclimate.com/v1/badges/670f08f9299cfab86748/maintainability)](https://codeclimate.com/github/whitehamster26/wh-converter/maintainability)
[![Build Status](https://travis-ci.org/whitehamster26/wh-converter.svg?branch=master)](https://travis-ci.org/whitehamster26/wh-converter)

<h2>Installation</h2>

<code>python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ wh-conv</code>

<h2>Usage</h2>

<h3>Check actual rate</h3>
<p>First you should pick a currency pair in format XXX-YYY. By default currency pair set USD-EUR</p>
<p>Just follow this command <code>wh-conv -p XXX-YYY</code> to set another pair</p>
<p>After that you can see actual rate of this pair just using <code>wh-conv</code></p>
<p><strong>Sometimes you can see "API error" exception.</strong></p>
<p>Unfortunately alphavantage (which API I use) doesn't support some currencies. If programm
doesn't able to parse server answer it throws this exception.</p>

<h3>Convert currency</h3>

<p>You can convert one currency to another just adding a number as an argument</p>
<code>wh-conv [NUMBER]</code><br>
<code>user@:~$ wh-conv<br>
USD-RUB: 68.68. Last update: 2020-06-06 13:48:52<br>
user@:~$ wh-conv 1000<br>
Converting USD-RUB: 1000 -> 68681.0</code>

<p>As a feature, you can change the pair and convert it immediately</p>
<code>user@:~$ wh-conv -p USD-CNY 1500<br>
Pair successfully changed to USD-CNY<br>
Converting USD-CNY: 1500 -> 10621.2<br>
</code>

<h3>Storage</h3>

<p>All data stores at your home directory so if you want to delete this app don't forget to delete the config file too.</p>
<p>Config file has name .wh-conv.json</p>



