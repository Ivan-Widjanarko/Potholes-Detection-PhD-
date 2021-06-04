package id.develo.capstoneproject.ui.authentication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import id.develo.capstoneproject.R

class AuthActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_auth)

        val mfragmentManager = supportFragmentManager
        val mLoginFragment = LoginFragment()
        val fragment = mfragmentManager.findFragmentByTag(LoginFragment::class.java.simpleName)

        if (fragment !is LoginFragment) {
            mfragmentManager
                .beginTransaction()
                .setCustomAnimations(R.anim.slide_in, R.anim.fade_out, R.anim.fade_in, R.anim.slide_out)
                .add(R.id.frame_container, mLoginFragment, LoginFragment::class.java.simpleName)
                .commit()
        }
    }
}