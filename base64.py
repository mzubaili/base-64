ó
 Wø[c           @   s°   d  d l  Z  d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z d Z d   Z	 d   Z
 d	   Z d
   Z d   Z y e   e   Wn e
   e d e  n Xd S(   iÿÿÿÿNs   [1;31ms   [1;32ms   [1;33ms   [1;36ms   [1;37mc          C   s9  d }  d } d } d } d } d } d } d } d	 } d
 }	 xö t  d  D]è }
 t j d  t j j d |  |
 t |   | |
 t |  | |
 t |  | |
 t |  | |
 t |  | |
 t |  | |
 t |  | |
 t |  | |
 t |  |	 |
 t |	  d  t j j   qI Wd  S(   Ns   processing          s   rocessing          ps   ocessing          prs   cessing          pros   essing          procs   ssing          proces   sing          process   ing          processs   ng          processis   g          processini)   g¹?s   [1;37m[ [1;36ms	    [1;37m](   t   ranget   timet   sleept   syst   stdoutt   writet   lent   flush(   t   pt   rt   ot   ct   et   st   St   it   nt   gt   a(    (    s	   base64.pyt   load   s    Èc           C   s   t  j d  d  S(   Nt   clear(   t   ost   system(    (    (    s	   base64.pyt   clr   s    c         C   sM   xF |  d D]: } t  j j |  t  j j   t j t j   d  q Wd  S(   Ns   
gq=
×£pÍ?(   R   R   R   R   R   R   t   random(   t   bR   (    (    s	   base64.pyt   asw   s    c           C   s   t    d t GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd GHd t t f GHd	 t t f GHd
 GHd  S(   Ns)     %s______                               s-      %s\  /   /\             %s _____ %s/) /)  s-      %s/ /_  (  )  _________ %s/ ___/%s/ // /  s-     %s/ __ \/ __ `/ ___/ _ \%s/ __ \%s/ // /_  s-    %s/ /_/ / /_/ (__  )  __%s/ (_/ %s/__  __/  s-   %s/_.___/\__,_/____/\___/%s\____/  %s/_/     s'                                          s+   %s Author: %sAnonyMass aka Zhu Bai Lee     s+   %scontact: %s082215885532                  t    (   R   t   cyt   mrt   pt(    (    (    s	   base64.pyt   logo%   s    	c          C   s  d t  GHd t  t f GHd t  t f GHd t  t f GHd t  t f GHd t  t f GHd t  GHt d t t f  }  |  d k s |  d	 k rØ t   t   t d
 t t f  } t   t   t   t j	 d |  n£|  d k sð |  d k r=t   t   t d t t f  } t   t   t   t j	 d |  n>|  d k sU|  d k r¨t   t   t d t t f  } t   t   t   t j	 d | | f  nÓ |  d k sÀ|  d k rt   t   t d t t f  } t   t   t   t j	 d | | f  nh |  d k s+|  d k rJt   t
   t d t  n1 d t |  f GHt j d  t   t   t   d  S(   Ns,   %s//////////////////////////////////////////s   %s[1] %sUbah text jadi base64s   %s[2] %sTranslate text base64s!   %s[3] %sBuat file tranlate base64s   %s[4] %sTranslate file base64s   %s[0] %sKeluars   %sPilih: %st   1t   01s   %sMasukkan text: %ss   echo %s | base64t   2t   02s   %sMasukkan text Base64: %ss   echo %s | base64 -dt   3t   03sB   %sMasukkan nama file
Contoh: /storage/emulated/0/contoh.html >> %ss   more %s | base64 >> %s.txtt   4t   04sI   %sMasukkan nama file base64
Contoh: /storage/emulated/0/contoh.html >> %ss   more %s | base64 -d >> %s.txtt   00t   0s*   %sTerima kasih telah menggunakan tools inis   %s%s not foundi   (   t   hjR   t	   raw_inputR   R   R   t   knR   R   R   t   exitR   R   R   t   isi(   R   R   R   t   dR   (    (    s	   base64.pyR.   2   sb    		s*   %sTerima kasih telah menggunakan tools ini(   R   R   R   R   R   R*   R,   R   R   R   R   R   R   R.   (    (    (    s	   base64.pyt   <module>   s$   					7