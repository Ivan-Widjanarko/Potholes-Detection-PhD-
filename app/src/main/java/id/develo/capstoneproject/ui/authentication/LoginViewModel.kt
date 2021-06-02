package id.develo.capstoneproject.ui.authentication

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import id.develo.capstoneproject.data.remote.api.ApiConfig
import id.develo.capstoneproject.data.remote.response.GetUserResponse
import id.develo.capstoneproject.utils.Event
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class LoginViewModel: ViewModel() {

    companion object {
        const val TAG = "LoginViewModel"
    }

    private var _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private var _isSuccess = MutableLiveData<Boolean>()
    val isSuccess: LiveData<Boolean> = _isSuccess

    private var _snackbarText = MutableLiveData<Event<String>>()
    val snackbarText: LiveData<Event<String>> = _snackbarText

    var idFromApi: Int? = 0

//    private val _emailFromApi = MutableLiveData<String>()
    var emailFromApi: String? = null

//    private val _passwordFromApi = MutableLiveData<String>()
    var passwordFromApi: String? = null

//    private val _deviceIdFromApi = MutableLiveData<Int>()
    var deviceIdFromApi: Int? = 0

    fun getUser(email: String, password: String) {
        _isLoading.value = true

        val client = ApiConfig.getApiService().userLogin(email, password)
        client.enqueue(object : Callback<GetUserResponse> {
            override fun onResponse(call: Call<GetUserResponse>, response: Response<GetUserResponse>) {
                _isLoading.value = false
                if (response.isSuccessful) {
                    if (response.body()?.status == "OK") {
                        _isSuccess.value = true
                        idFromApi = response.body()?.userInfo?.id
                        emailFromApi = response.body()?.userInfo?.email
                        passwordFromApi = response.body()?.userInfo?.password
                        deviceIdFromApi = response.body()?.userInfo?.deviceId
                        _snackbarText.value = Event("${response.body()?.message}")
                    } else {
                        _isSuccess.value = false
                        _snackbarText.value = Event("${response.body()?.message}")
                    }

                } else {
                    _isSuccess.value = false
                    Log.e(TAG, "GAGAL: ${response.message()}")
                }
            }

            override fun onFailure(call: Call<GetUserResponse>, t: Throwable) {
                _isSuccess.value = false
                _isLoading.value = false
                Log.e(TAG, "onFailure: ${t.message.toString()}")
            }
        })
    }
}