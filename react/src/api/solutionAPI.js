class SolutionApi {
  // let baseUrl = "http://localhost:8000";
  let baseUrl = ''
  /* BEGIN MAKE REQUEST */
  static makeRequest(url, method, body) {
    // let token = localStorage.getItem(environmentConstants.TOKEN_KEY);
    let token = '123'
    return new Promise((resolve, reject) => {
      fetch(baseUrl + url, {
        method: method,
        body: body,
        mode: 'cors',
        headers: {
          'token': token,
          'Accept': 'application/json; charset=utf-8',
          'Content-Type': 'application/json'

        }
      }).catch(response => {
        /* This gets called when fetch fails (i.e. network error) */
        return reject(response);
      }).then(response => {
        if (!response.ok) {
          if (response.status === 401) {
            // localStorage.removeItem(environmentConstants.TOKEN_KEY);
            browserHistory.push('/access-denied');
            return reject('Error:  Unauthorized Prudena API call');
          }
          /* fetch worked but not a 200 - 299 status code */
          try {
            return response.json().then(json => {
              return reject(JSON.stringify(json));
            });
          } catch (e) {
            return reject(JSON.stringify(response));
          }
        } else {
          return resolve(response.json());
        }
      });
    });
  }

  // static getSolutionLibraryByUser() {
  //   return makeRequest('/api/')''
  // }

}