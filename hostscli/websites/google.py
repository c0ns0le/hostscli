#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: google.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-01-15
"""

DOMAINS = [
    "1e100.net",
    "466453.com",
    "admob.com",
    "adsense.com",
    "adwords.com",
    "android.com",
    "blogger.com",
    "blogspot.com",
    "chrome.com",
    "chromebook.com",
    "chromium.org",
    "cobrasearch.com",
    "com.google",
    "domains.google",
    "doubleclick.com",
    "duck.com",
    "feedburner.com",
    "firehunt.com",
    "foofle.com",
    "froogle.com",
    "g.cn",
    "g.co",
    "ggoogle.com",
    "ggpht.com",
    "gmail.com",
    "gmodules.com",
    "gogle.com",
    "gogole.com",
    "goo.gl",
    "googel.com",
    "googil.com",
    "googl.com",
    "google-analytics.com",
    "google.ac",
    "google.ad",
    "google.ae",
    "google.al",
    "google.am",
    "google.as",
    "google.at",
    "google.az",
    "google.ba",
    "google.be",
    "google.bf",
    "google.bg",
    "google.bi",
    "google.bj",
    "google.bs",
    "google.bt",
    "google.by",
    "google.ca",
    "google.cat",
    "google.cc",
    "google.cd",
    "google.cf",
    "google.cg",
    "google.ch",
    "google.ci",
    "google.cl",
    "google.cm",
    "google.cn",
    "google.co.ao",
    "google.co.bw",
    "google.co.ck",
    "google.co.cr",
    "google.co.id",
    "google.co.il",
    "google.co.in",
    "google.co.jp",
    "google.co.ke",
    "google.co.kr",
    "google.co.ls",
    "google.co.ma",
    "google.co.mz",
    "google.co.nz",
    "google.co.th",
    "google.co.tz",
    "google.co.ug",
    "google.co.uk",
    "google.co.uz",
    "google.co.ve",
    "google.co.vi",
    "google.co.za",
    "google.co.zm",
    "google.co.zw",
    "google.com",
    "google.com",
    "google.com.af",
    "google.com.ag",
    "google.com.ai",
    "google.com.ar",
    "google.com.au",
    "google.com.bd",
    "google.com.bh",
    "google.com.bn",
    "google.com.bo",
    "google.com.br",
    "google.com.bz",
    "google.com.co",
    "google.com.cu",
    "google.com.cy",
    "google.com.do",
    "google.com.ec",
    "google.com.eg",
    "google.com.et",
    "google.com.fj",
    "google.com.gh",
    "google.com.gi",
    "google.com.gt",
    "google.com.hk",
    "google.com.jm",
    "google.com.kh",
    "google.com.kw",
    "google.com.lb",
    "google.com.lc",
    "google.com.ly",
    "google.com.mm",
    "google.com.mt",
    "google.com.mx",
    "google.com.my",
    "google.com.na",
    "google.com.nf",
    "google.com.ng",
    "google.com.ni",
    "google.com.np",
    "google.com.om",
    "google.com.pa",
    "google.com.pe",
    "google.com.pg",
    "google.com.ph",
    "google.com.pk",
    "google.com.pr",
    "google.com.py",
    "google.com.qa",
    "google.com.sa",
    "google.com.sb",
    "google.com.sg",
    "google.com.sl",
    "google.com.sv",
    "google.com.tj",
    "google.com.tr",
    "google.com.tw",
    "google.com.ua",
    "google.com.uy",
    "google.com.vc",
    "google.com.vn",
    "google.cv",
    "google.cz",
    "google.de",
    "google.dj",
    "google.dk",
    "google.dm",
    "google.dz",
    "google.ee",
    "google.es",
    "google.fi",
    "google.fm",
    "google.fr",
    "google.ga",
    "google.ge",
    "google.gf",
    "google.gg",
    "google.gl",
    "google.gm",
    "google.gp",
    "google.gr",
    "google.gy",
    "google.hn",
    "google.hr",
    "google.ht",
    "google.hu",
    "google.ie",
    "google.im",
    "google.io",
    "google.iq",
    "google.is",
    "google.it",
    "google.je",
    "google.jo",
    "google.kg",
    "google.ki",
    "google.kz",
    "google.la",
    "google.li",
    "google.lk",
    "google.lt",
    "google.lu",
    "google.lv",
    "google.md",
    "google.me",
    "google.mg",
    "google.mk",
    "google.ml",
    "google.mn",
    "google.ms",
    "google.mu",
    "google.mv",
    "google.mw",
    "google.ne",
    "google.net",
    "google.nl",
    "google.no",
    "google.nr",
    "google.nu",
    "google.org",
    "google.pl",
    "google.pn",
    "google.ps",
    "google.pt",
    "google.ro",
    "google.rs",
    "google.ru",
    "google.rw",
    "google.sc",
    "google.se",
    "google.sh",
    "google.si",
    "google.sk",
    "google.sm",
    "google.sn",
    "google.so",
    "google.sr",
    "google.st",
    "google.td",
    "google.tg",
    "google.tk",
    "google.tl",
    "google.tm",
    "google.tn",
    "google.to",
    "google.tt",
    "google.vg",
    "google.vu",
    "google.ws",
    "googleadservices.com",
    "googleanalytics.com",
    "googleapis.com",
    "googleapps.com",
    "googlearth.com",
    "googlebot.com",
    "googlecode.com",
    "googlecommerce.com",
    "googledrive.com",
    "googlee.com",
    "googleearth.com",
    "googlemail.com",
    "googlemaps.com",
    "googlepagecreator.com",
    "googlescholar.com",
    "googlesource.com",
    "googlesyndication.com",
    "googletagmanager.com",
    "googleusercontent.com",
    "googlr.com",
    "goolge.com",
    "gooogle.com",
    "igoogle.com",
    "keyhole.com",
    "like.com",
    "localhost.com",
    "madewithcode.com",
    "panoramio.com",
    "picasa.com",
    "sketchup.com",
    "urchin.com",
    "waze.com",
    "whatbrowser.org",
    "withgoogle.com",
    "youtu.be",
    "youtube-nocookie.com",
    "youtube.com",
    "youtubeeducation.com",
    "youtubegaming.com",
    "yt.be",
    "ytimg.com",
]