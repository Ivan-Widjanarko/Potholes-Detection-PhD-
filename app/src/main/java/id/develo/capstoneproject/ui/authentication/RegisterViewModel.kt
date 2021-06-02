package id.develo.capstoneproject.ui.authentication

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import id.develo.capstoneproject.data.local.entity.UserEntity
import id.develo.capstoneproject.data.remote.api.ApiConfig
import id.develo.capstoneproject.data.remote.response.PostUserResponse
import id.develo.capstoneproject.utils.Event
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class RegisterViewModel: ViewModel() {

    companion object {
        const val TAG = "RgisterViewModel"
    }

    private var _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private var _isSuccess = MutableLiveData<Boolean>()
    val isSuccess: LiveData<Boolean> = _isSuccess

    private var _snackbarText = MutableLiveData<Event<String>>()
    val snackbarText: LiveData<Event<String>> = _snackbarText

    fun registerUser(email: String, password: String, deviceId: Int) {
        _isLoading.value = true

        val client = ApiConfig.getApiService().userRegister(email, password, deviceId)
        client.enqueue(object : Callback<PostUserResponse> {
            override fun onResponse(call: Call<PostUserResponse>, response: Response<PostUserResponse>) {
                _isLoading.value = false
                if (response.isSuccessful) {
                    if(response.body()?.status == "OK") {
                        _snackbarText.value = Event("${response.body()?.message}")
                        _isSuccess.value = true
                    } else {
                        _snackbarText.value = Event("${response.body()?.message}")
                        _isSuccess.value = false
                    }

                } else {
                    _isSuccess.value = false
                    Log.e(TAG, "onFailure: ${response.message()}")
                }
            }

            override fun onFailure(call: Call<PostUserResponse>, t: Throwable) {
                _isLoading.value = false
                Log.e(TAG, "onFailure: ${t.message.toString()}")
            }
        })
    }
}