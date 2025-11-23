# एजेंट स्कैफोल्डर

टेक्स्ट फ़ाइल विवरण से स्वचालित रूप से प्रोजेक्ट संरचनाएं बनाने के लिए एक Python टूल।

## विशेषताएं

- एक सरल टेक्स्ट फ़ाइल से पूर्ण प्रोजेक्ट डायरेक्टरी संरचनाएं बनाएं
- स्वचालित रूप से प्लेसहोल्डर फ़ाइलें उत्पन्न करता है
- नेस्टेड डायरेक्टरी संरचनाओं का समर्थन करता है
- उपयोग में आसान कमांड-लाइन इंटरफ़ेस

## इंस्टॉलेशन

```bash
pip install -e .
```

या Poetry का उपयोग करके:

```bash
poetry install
```

## उपयोग

```bash
python src/scaffolder.py <structure_file> <destination>
```

### उदाहरण

```bash
python src/scaffolder.py example.txt ./my_new_project
```

यह `example.txt` फ़ाइल के आधार पर `./my_new_project` डायरेक्टरी में एक प्रोजेक्ट संरचना बनाएगा।

## संरचना फ़ाइल प्रारूप

संरचना फ़ाइल को ट्री जैसे प्रारूप का उपयोग करना चाहिए:

```
project_name/
├── src/
│   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
├── README.md
└── setup.py
```

## आवश्यकताएं

- Python 3.9+

## लाइसेंस

विवरण के लिए LICENSE फ़ाइल देखें।

## योगदान

योगदान का स्वागत है! कृपया बेझिझक Pull Request सबमिट करें।

---

**अन्य भाषाएं:**
- [English](README.md)
- [Français (French)](README.fr.md)
