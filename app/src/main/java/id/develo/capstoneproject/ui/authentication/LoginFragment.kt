package id.develo.capstoneproject.ui.authentication

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.FragmentActivity
import id.develo.capstoneproject.MainActivity
import id.develo.capstoneproject.R
import id.develo.capstoneproject.databinding.FragmentLoginBinding
import id.develo.capstoneproject.ui.about.AboutActivity


class LoginFragment : Fragment() {

    private var _binding: FragmentLoginBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        _binding = FragmentLoginBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.btnLogin.setOnClickListener {
            Intent(activity, MainActivity::class.java).also {
                startActivity(it)
            }
        }

        binding.tvSignup.setOnClickListener {
            // Move to Register Page
            moveToRegister()
        }
    }

    private fun moveToRegister() {
        val mRegisterFragment = RegisterFragment()
        val mFragmentManager = parentFragmentManager
        mFragmentManager.beginTransaction().apply {
            setCustomAnimations(R.anim.slide_in, R.anim.fade_out, R.anim.fade_in, R.anim.slide_out)
            replace(
                R.id.frame_container,
                mRegisterFragment,
                RegisterFragment::class.java.simpleName
            )
            addToBackStack(null)
            commit()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}