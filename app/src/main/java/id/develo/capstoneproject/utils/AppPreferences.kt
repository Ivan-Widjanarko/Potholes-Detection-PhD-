package id.develo.capstoneproject.utils

import android.content.Context
import android.content.SharedPreferences

object AppPreferences {
    private const val NAME = "PotHoleDetection"
    private const val MODE = Context.MODE_PRIVATE
    private lateinit var preferences: SharedPreferences

    // SharedPreferences variables
    private val UID = Pair("uid", 0)
    private val DEVICE_ID = Pair("device_id", 0)
    private val EMAIL = Pair("email", "")
    private val PASSWORD = Pair("password", "")
    private val IS_LOGIN = Pair("is_login", false)

    fun init(context: Context) {
        preferences = context.getSharedPreferences(NAME, MODE)
    }

    //an inline function to put variable and save it
    private inline fun SharedPreferences.edit(operation: (SharedPreferences.Editor) -> Unit) {
        val editor = edit()
        operation(editor)
        editor.apply()
    }

    //SharedPreferences variables getters/setters
    var isLogin: Boolean
        get() = preferences.getBoolean(IS_LOGIN.first, IS_LOGIN.second)
        set(value) = preferences.edit {
            it.putBoolean(IS_LOGIN.first, value)
        }

    var uId: Int
        get() = preferences.getInt(UID.first, UID.second)
        set(value) = preferences.edit {
            it.putInt(UID.first, value)
        }

    var deviceId: Int
        get() = preferences.getInt(DEVICE_ID.first, DEVICE_ID.second)
        set(value) = preferences.edit {
            it.putInt(DEVICE_ID.first, value)
        }

    var email: String
        get() = preferences.getString(EMAIL.first, EMAIL.second) ?: ""
        set(value) = preferences.edit {
            it.putString(EMAIL.first, value)
        }

    var password: String
        get() = preferences.getString(PASSWORD.first, PASSWORD.second) ?: ""
        set(value) = preferences.edit {
            it.putString(PASSWORD.first, value)
        }

}