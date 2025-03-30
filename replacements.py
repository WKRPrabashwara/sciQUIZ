replacements_list = [
    ["&quot;", '"'],  ["&#34;", '"'],    # Double quotation mark
    ["&apos;", "'"],  ["&#39;", "'"],    # Apostrophe
    ["&amp;", "&"],   ["&#38;", "&"],    # Ampersand
    ["&lt;", "<"],    ["&#60;", "<"],    # Less-than sign
    ["&gt;", ">"],    ["&#62;", ">"],    # Greater-than sign
    ["&nbsp;", " "],  ["&#160;", " "],   # Non-breaking space
    ["&iexcl;", "¡"], ["&#161;", "¡"],   # Inverted exclamation mark
    ["&cent;", "¢"],  ["&#162;", "¢"],   # Cent sign
    ["&pound;", "£"], ["&#163;", "£"],   # Pound sign
    ["&yen;", "¥"],   ["&#165;", "¥"],   # Yen sign
    ["&euro;", "€"],  ["&#8364;", "€"],  # Euro sign
    ["&copy;", "©"],  ["&#169;", "©"],   # Copyright sign
    ["&reg;", "®"],   ["&#174;", "®"],   # Registered trademark sign
    ["&trade;", "™"], ["&#8482;", "™"],  # Trademark sign
    ["&deg;", "°"],   ["&#176;", "°"],   # Degree symbol
    ["&plusmn;", "±"],["&#177;", "±"],   # Plus-minus sign
    ["&times;", "×"], ["&#215;", "×"],   # Multiplication sign
    ["&divide;", "÷"],["&#247;", "÷"],   # Division sign
    ["&permil;", "‰"],["&#8240;", "‰"],  # Per mille sign
    ["&micro;", "µ"], ["&#181;", "µ"],   # Micro sign
    ["&para;", "¶"],  ["&#182;", "¶"],   # Paragraph sign
    ["&sect;", "§"],  ["&#167;", "§"],   # Section sign
    ["&sup1;", "¹"],  ["&#185;", "¹"],   # Superscript 1
    ["&sup2;", "²"],  ["&#178;", "²"],   # Superscript 2
    ["&sup3;", "³"],  ["&#179;", "³"],   # Superscript 3
    ["&frac14;", "¼"],["&#188;", "¼"],   # Fraction 1/4
    ["&frac12;", "½"],["&#189;", "½"],   # Fraction 1/2
    ["&frac34;", "¾"],["&#190;", "¾"],   # Fraction 3/4
    ["&middot;", "·"],["&#183;", "·"],   # Middle dot
    ["&hellip;", "…"],["&#8230;", "…"],  # Ellipsis
    ["&ndash;", "–"], ["&#8211;", "–"],  # En dash
    ["&mdash;", "—"], ["&#8212;", "—"],  # Em dash
    ["&lsquo;", "‘"], ["&#8216;", "‘"],  # Left single quote
    ["&rsquo;", "’"], ["&#8217;", "’"],  # Right single quote
    ["&ldquo;", "“"], ["&#8220;", "“"],  # Left double quote
    ["&rdquo;", "”"], ["&#8221;", "”"],  # Right double quote
    ["&lsaquo;", "‹"],["&#8249;", "‹"],  # Single left-pointing angle quote
    ["&rsaquo;", "›"],["&#8250;", "›"],  # Single right-pointing angle quote
    ["&laquo;", "«"], ["&#171;", "«"],   # Left double angle quote
    ["&raquo;", "»"], ["&#187;", "»"],   # Right double angle quote
    ["&bull;", "•"],  ["&#8226;", "•"],  # Bullet
    ["&starf;", "★"], ["&#9733;", "★"],  # Filled star
    ["&empty;", "∅"], ["&#8709;", "∅"],  # Empty set
    ["&infin;", "∞"], ["&#8734;", "∞"],  # Infinity
    ["&radic;", "√"], ["&#8730;", "√"],  # Square root
    ["&sum;", "∑"],   ["&#8721;", "∑"],  # Summation
    ["&prod;", "∏"],  ["&#8719;", "∏"],  # Product
    ["&int;", "∫"],   ["&#8747;", "∫"],  # Integral
    ["&part;", "∂"],  ["&#8706;", "∂"],  # Partial differential
    ["&asymp;", "≈"], ["&#8776;", "≈"],  # Approximately equal
    ["&ne;", "≠"],    ["&#8800;", "≠"],  # Not equal
    ["&le;", "≤"],    ["&#8804;", "≤"],  # Less than or equal
    ["&ge;", "≥"],    ["&#8805;", "≥"],  # Greater than or equal
    ["&sub;", "⊂"],   ["&#8834;", "⊂"],  # Subset
    ["&sup;", "⊃"],   ["&#8835;", "⊃"],  # Superset
    ["&nsub;", "⊄"],  ["&#8836;", "⊄"],  # Not a subset
    ["&isin;", "∈"],  ["&#8712;", "∈"],  # Element of
    ["&notin;", "∉"], ["&#8713;", "∉"],  # Not an element of
    ["&ang;", "∠"],   ["&#8736;", "∠"],  # Angle
    ["&there4;", "∴"],["&#8756;", "∴"],  # Therefore symbol
    ["&perp;", "⊥"],  ["&#8869;", "⊥"],  # Perpendicular
    ["&sdot;", "⋅"],  ["&#8901;", "⋅"],  # Dot operator
    ["&larr;", "←"],  ["&#8592;", "←"],  # Left arrow
    ["&rarr;", "→"],  ["&#8594;", "→"],  # Right arrow
    ["&uarr;", "↑"],  ["&#8593;", "↑"],  # Up arrow
    ["&darr;", "↓"],  ["&#8595;", "↓"],  # Down arrow
    ["&harr;", "↔"],  ["&#8596;", "↔"],  # Left-right arrow
    ["&crarr;", "↵"], ["&#8629;", "↵"],  # Carriage return arrow
    ["&lceil;", "⌈"], ["&#8968;", "⌈"],  # Left ceiling
    ["&rceil;", "⌉"], ["&#8969;", "⌉"],  # Right ceiling
    ["&lfloor;", "⌊"],["&#8970;", "⌊"],  # Left floor
    ["&rfloor;", "⌋"],["&#8971;", "⌋"],  # Right floor
    ["&loz;", "◊"],   ["&#9674;", "◊"],  # Lozenge
    ["&spades;", "♠"],["&#9824;", "♠"],  # Spade suit
    ["&clubs;", "♣"], ["&#9827;", "♣"],  # Club suit
    ["&hearts;", "♥"],["&#9829;", "♥"],  # Heart suit
    ["&diams;", "♦"], ["&#9830;", "♦"],  # Diamond suit
    ["&#039;", "'"], ["&ouml;", "ö"], 
]