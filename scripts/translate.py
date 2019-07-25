#-*- coding:utf-8 -*-

import requests

LANGS = {
".link1" : "Blockchain 101",
".link2" : "Hackathon",
".link3" : "Toolsets",
".link4" : "Examples",
"#main_title" : "Quorum Korea Toolkits & Examples",
"#main_subtitle1" : "This site is the hub for Quorum Korea's Toolkits and repositories. Here, you can find easy access to a variety of translated docs, helpful code bits, and examples to help you develop on Quorum.",
"#main_subtitle2" : "If you know blockchain and Ethereum already click the button below. If you are a beginner, check out the 'Start Here' section above.",
"#main_button1" : "Jump In!",
"#sec_header1" : "Toolsets",
"#sec_sub1" : "Some helpful tools for building Quorum apps.",
"#tool_descrip1" : "This Repo is the main repo for Quorum's Eth-based Blockchain solution",
"#tool_descrip2" : "Enterprise Implementation of Quorum's transaction manager",
"#tool_descrip3" : "An integrated development environment and SDK for Ethereum-like ledgers",
"#tool_descrip4" : "A Peer-to-peer encrypted message exchange",
"#tool_descrip5" : "This project contains tools for running Quorum clusters and integration testing Quorum.",
"#tool_descrip6" : "Deploy Quorum network in a cloud provider of choice",
"#sec2_header" : "Examples",
"#sec2_sub" : "Examples of Quorum Usage and Chain Deployment",
"#sec2_header1" : "TESTING",
"#sec2_body1" : "Starts up a fully-functioning Quorum environment consisting of 7 independent nodes. From this example one can test consensus, privacy, and all the expected functionality of an Ethereum platform.",
"#sec2_header2" : "SIMULATION",
"#sec2_body2" : "Starts up a set of 5 nodes that simulates a Real-time Gross Setlement environment with 3 banks, one regulator (typically a central bank) and an observer that cannot access the private data.",
"#sec2_header3" : "DAPP EXAMPLE",
"#sec2_body3" : "Basic Dapp demonstrating Hashing of a File and Saving it to a basic Quorum Blockchain. Requires access to a Quorum RPC to run.",
".drop_sec1" : "1.) Understanding Quorum",
".drop_sub1" : "Quorum 101",
".drop_sec2" : "2.) Getting Setup",
".drop_sub2" : "Get a Quorum Chain Going",
".drop_sec3" : "3.) Using Quorum",
".drop_sub3" : "Start Developing",
".drop_sec4" : "FAQ",
".drop_sub4" : "Frequently Asked Questions",
".drop_sec5" : "Ethereum",
".drop_sub5" : "Understanding Ethereum",
".drop_sec6" : "API",
".drop_sub6" : "Web3 & Quorum (EN)",
".drop_sec7" : "View Full Wiki",
".drop_sub7" : "Checkout Korean Wiki on Github",
".drop_sec8" : "Enterprise Blockchain",
".drop_sub8" : "Download Enterprise Blockchain Deck",
".drop_cc_title" : "Main Repository",
".drop_cc_body" : "This is the official Quorum Repository (English)"
}


#ENDPOINT = "https://openapi.naver.com/v1/papago/n2mt"
ENDPOING = "https://translation.googleapis.com"
#fields
SOURCE = "영어"
TARGET = "한국어"
#text

def translateChunk(_text):
    resp = requests.post(ENDPOINT, data={"target": TARGET, "source": SOURCE, "text": _text})
    print(resp.content)
    return resp.content

retDict = {}

for key in LANGS:
    text = LANGS.get(key)
    retDict[key] = translateChunk(text)


print(retDict)
