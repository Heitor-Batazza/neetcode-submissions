class TimeMap {
map<string, vector<pair<string, int>>> keyStore;
public:
    TimeMap() {
        keyStore = {};
    }
    
    void set(string key, string value, int timestamp) {
        if (keyStore.count(key) == 0) {
            keyStore[key] = {{value, timestamp}};
        } else {
            keyStore[key].push_back({value, timestamp});
        }
    }
    
    string get(string key, int timestamp) {
        int l;
        int r;
        int m;

        string res = "";
        auto& values = keyStore[key];

        l = 0;
        r = (int)values.size() - 1;

        while (l <= r) {
            m = (l + r) / 2;
            if (values[m].second <= timestamp) {
                res = values[m].first;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return res;
    }
};
